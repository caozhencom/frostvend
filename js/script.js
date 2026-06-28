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
    const angleBtns = document.querySelectorAll('.viewer-360-angle-btn');

    if (!viewer) return;

    // 图片数组
    const images = [
        'images/product/1.png',
        'images/product/2.png',
        'images/product/3.png',
        'images/product/4.png'
    ];

    let isDragging = false;
    let startX = 0;
    let currentRotation = 0;
    let autoRotate = true;
    let currentAngle = 0;

    // 初始化
    viewer.style.transform = 'rotateY(0deg)';

    // 切换图片
    function switchImage(angleIndex) {
        currentAngle = angleIndex;
        if (mainImage && images[angleIndex]) {
            mainImage.src = images[angleIndex];
        }
        // 更新按钮状态
        angleBtns.forEach((btn, index) => {
            btn.classList.toggle('active', index === angleIndex);
        });
    }

    // 角度切换按钮事件
    angleBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            switchImage(index);
        });
    });

    // 拖动开始
    function handleDragStart(e) {
        isDragging = true;
        startX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;

        // 暂停自动旋转
        if (autoRotate) {
            viewer.classList.add('paused');
        }

        // 获取当前旋转角度
        const transform = getComputedStyle(viewer).transform;
        if (transform !== 'none') {
            const matrix = transform.split('(')[1].split(')')[0].split(',');
            const a = parseFloat(matrix[0]);
            const b = parseFloat(matrix[1]);
            currentRotation = Math.round(Math.atan2(b, a) * (180 / Math.PI));
            if (currentRotation < 0) currentRotation += 360;
        }
    }

    // 拖动移动
    function handleDragMove(e) {
        if (!isDragging) return;

        const clientX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
        const deltaX = clientX - startX;

        // 计算新的旋转角度
        const newRotation = currentRotation + (deltaX * 0.5);
        viewer.style.transform = `rotateY(${newRotation}deg)`;
    }

    // 拖动结束
    function handleDragEnd() {
        if (!isDragging) return;
        isDragging = false;

        // 更新当前角度
        const transform = getComputedStyle(viewer).transform;
        if (transform !== 'none') {
            const matrix = transform.split('(')[1].split(')')[0].split(',');
            const a = parseFloat(matrix[0]);
            const b = parseFloat(matrix[1]);
            currentRotation = Math.round(Math.atan2(b, a) * (180 / Math.PI));
        }
    }

    // 鼠标事件
    viewer.addEventListener('mousedown', handleDragStart);
    document.addEventListener('mousemove', handleDragMove);
    document.addEventListener('mouseup', handleDragEnd);

    // 触摸事件
    viewer.addEventListener('touchstart', handleDragStart, { passive: true });
    document.addEventListener('touchmove', handleDragMove, { passive: true });
    document.addEventListener('touchend', handleDragEnd);

    // 自动旋转按钮
    if (btnAutoRotate) {
        btnAutoRotate.addEventListener('click', () => {
            autoRotate = !autoRotate;

            if (autoRotate) {
                viewer.classList.add('auto-rotate');
                viewer.classList.remove('paused');
                btnAutoRotate.classList.add('active');
            } else {
                viewer.classList.remove('auto-rotate');
                viewer.classList.remove('paused');
                btnAutoRotate.classList.remove('active');

                // 保持在当前角度
                const transform = getComputedStyle(viewer).transform;
                if (transform !== 'none') {
                    const matrix = transform.split('(')[1].split(')')[0].split(',');
                    const a = parseFloat(matrix[0]);
                    const b = parseFloat(matrix[1]);
                    currentRotation = Math.round(Math.atan2(b, a) * (180 / Math.PI));
                    viewer.style.transform = `rotateY(${currentRotation}deg)`;
                }
            }
        });
    }

    // 重置按钮
    if (btnReset) {
        btnReset.addEventListener('click', () => {
            currentRotation = 0;
            viewer.style.transform = 'rotateY(0deg)';

            // 恢复自动旋转
            if (!autoRotate) {
                autoRotate = true;
                viewer.classList.add('auto-rotate');
                viewer.classList.remove('paused');
                if (btnAutoRotate) btnAutoRotate.classList.add('active');
            }
        });
    }
})();
