document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.slide');
    const slider = document.querySelector('.slider');
    const totalSlides = slides.length;

    function updateSlider(index) {
        slider.style.transition = 'transform 0.5s ease-in-out';
        slider.style.transform = `translateX(-${index * 100}%)`;
    }

    // 자동 슬라이더
    let slideInterval = setInterval(() => {
        if (currentIndex === totalSlides - 1) {
            // 마지막 슬라이드에서 첫 슬라이드로 이동할 때
            slider.style.transition = 'transform 0.5s ease-in-out'; // 애니메이션 효과 유지
            currentIndex = 0; // 첫 슬라이드로 이동
            updateSlider(currentIndex);
        } else {
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider(currentIndex);
        }
    }, 5000);

    // 이전 및 다음 버튼 기능
    document.querySelector('.prev').addEventListener('click', () => {
        clearInterval(slideInterval); // 자동 슬라이드 일시 중지
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        updateSlider(currentIndex);
        slideInterval = setInterval(() => { // 자동 슬라이드 재시작
            if (currentIndex === totalSlides - 1) {
                slider.style.transition = 'transform 0.5s ease-in-out';
                currentIndex = 0;
                updateSlider(currentIndex);
            } else {
                currentIndex = (currentIndex + 1) % totalSlides;
                updateSlider(currentIndex);
            }
        }, 5000);
    });

    document.querySelector('.next').addEventListener('click', () => {
        clearInterval(slideInterval); // 자동 슬라이드 일시 중지
        if (currentIndex === totalSlides - 1) {
            slider.style.transition = 'transform 0.5s ease-in-out';
            currentIndex = 0;
            updateSlider(currentIndex);
        } else {
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider(currentIndex);
        }
        slideInterval = setInterval(() => { // 자동 슬라이드 재시작
            if (currentIndex === totalSlides - 1) {
                slider.style.transition = 'transform 0.5s ease-in-out';
                currentIndex = 0;
                updateSlider(currentIndex);
            } else {
                currentIndex = (currentIndex + 1) % totalSlides;
                updateSlider(currentIndex);
            }
        }, 5000);
    });
});
