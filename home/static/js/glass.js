function fillGlass(percent) {
    // Находим элемент заполнения стакана
    const fillElement = document.querySelector('.fill');

    // Рассчитываем высоту заполнения в пикселях в зависимости от процента
    const aquaImgHeight = document.querySelector('.aqua-img').offsetHeight;
    const fillHeight = (percent / 100) * aquaImgHeight;

    // Устанавливаем высоту элемента заполнения
    fillElement.style.height = fillHeight + 'px';
}
