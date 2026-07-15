// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// 移动端菜单切换
const navToggle = document.getElementById('navToggle');
const navMenu = document.querySelector('.nav-menu');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
        if (navMenu.style.display === 'flex') {
            navMenu.style.flexDirection = 'column';
            navMenu.style.position = 'absolute';
            navMenu.style.top = '60px';
            navMenu.style.left = '0';
            navMenu.style.right = '0';
            navMenu.style.background = 'rgba(30, 58, 95, 0.98)';
            navMenu.style.padding = '20px';
        }
    });
}

// 导航栏滚动效果
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 100) {
        navbar.style.background = 'rgba(30, 58, 95, 0.98)';
    } else {
        navbar.style.background = 'rgba(30, 58, 95, 0.95)';
    }
    lastScroll = currentScroll;
});

// 表单提交
const form = document.querySelector('form');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('感谢您的提交！我们会尽快与您联系。');
        this.reset();
    });
}

// 数字动画
function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        element.textContent = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// 滚动到可视区域时触发动画
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// 观察所有section
document.querySelectorAll('.section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.6s, transform 0.6s';
    observer.observe(section);
});

console.log('雪糕自动售货机官网已加载');

// ==================== 360度展示功能 ====================
(function() {
    const viewer = document.getElementById('viewer360');
    const btnAutoRotate = document.getElementById('btnAutoRotate');
    const btnReset = document.getElementById('btnReset');
    const mainImage = document.getElementById('mainImage');
    const angleBtns = Array.from(document.querySelectorAll('.viewer-360-angle-btn'));

    if (!viewer || !mainImage || angleBtns.length === 0) return;

    const images = angleBtns
        .map((btn) => btn.querySelector('img'))
        .filter(Boolean)
        .map((img) => img.getAttribute('src'));

    if (images.length === 0) return;

    images.forEach((src) => {
        const preload = new Image();
        preload.src = src;
    });

    const dragStep = 32;
    const autoRotateDelay = 900;

    let isDragging = false;
    let startX = 0;
    let lastX = 0;
    let dragOffset = 0;
    let currentAngle = 0;
    let autoRotate = true;
    let autoRotateTimer = null;

    function normalizeIndex(index) {
        return (index + images.length) % images.length;
    }

    function switchImage(angleIndex) {
        currentAngle = normalizeIndex(angleIndex);
        mainImage.src = images[currentAngle];
        angleBtns.forEach((btn, index) => {
            btn.classList.toggle('active', index === currentAngle);
        });
    }

    function stopAutoRotate() {
        autoRotate = false;
        if (autoRotateTimer) {
            window.clearInterval(autoRotateTimer);
            autoRotateTimer = null;
        }
        btnAutoRotate?.classList.remove('active');
    }

    function startAutoRotate() {
        if (images.length < 2) return;
        stopAutoRotate();
        autoRotate = true;
        btnAutoRotate?.classList.add('active');
        autoRotateTimer = window.setInterval(() => {
            switchImage(currentAngle + 1);
        }, autoRotateDelay);
    }

    function handleDragStart(e) {
        isDragging = true;
        startX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
        lastX = startX;
        dragOffset = 0;
        viewer.classList.add('dragging');
        stopAutoRotate();
    }

    function handleDragMove(e) {
        if (!isDragging) return;

        const clientX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
        const deltaX = clientX - lastX;
        lastX = clientX;
        dragOffset += deltaX;

        if (e.cancelable) {
            e.preventDefault();
        }

        while (Math.abs(dragOffset) >= dragStep) {
            const direction = dragOffset > 0 ? -1 : 1;
            switchImage(currentAngle + direction);
            dragOffset += direction * dragStep;
        }
    }

    function handleDragEnd() {
        if (!isDragging) return;
        isDragging = false;
        dragOffset = 0;
        viewer.classList.remove('dragging');
    }

    angleBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            stopAutoRotate();
            switchImage(index);
        });
    });

    viewer.addEventListener('mousedown', handleDragStart);
    document.addEventListener('mousemove', handleDragMove);
    document.addEventListener('mouseup', handleDragEnd);
    viewer.addEventListener('mouseleave', handleDragEnd);

    viewer.addEventListener('touchstart', handleDragStart, { passive: true });
    document.addEventListener('touchmove', handleDragMove, { passive: false });
    document.addEventListener('touchend', handleDragEnd);
    document.addEventListener('touchcancel', handleDragEnd);

    if (btnAutoRotate) {
        btnAutoRotate.addEventListener('click', () => {
            if (autoRotateTimer) {
                stopAutoRotate();
                return;
            }
            startAutoRotate();
        });
    }

    if (btnReset) {
        btnReset.addEventListener('click', () => {
            switchImage(0);
            startAutoRotate();
        });
    }

    switchImage(0);
    startAutoRotate();
})();
