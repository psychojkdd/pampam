function val() {
    let list = document.getElementById("list");
    if (list.classList.contains("show")) {
        list.classList.remove("show");
    } else {
        list.classList.add("show");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const contentBlocks = document.querySelectorAll('.content-block');

    function checkVisibility() {
        const windowHeight = window.innerHeight;
        contentBlocks.forEach(function (block) {
            const rect = block.getBoundingClientRect();
            if (rect.top <= windowHeight * 0.75) {
                block.classList.add('show');
            }
        });
    }

    checkVisibility(); // Проверим видимость сразу при загрузке страницы

    window.addEventListener('scroll', checkVisibility); // Проверка видимости при скролле
});