var myMap;

ymaps.ready(init);

function init()
{
    myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 10
    });
    for (var p in police)
    {
        // Создание метки.
        var myGeoObject = new ymaps.Placemark(police[p][0], // координаты точки
            { balloonContent: '<a href="/calls/' + police[p][1].toString() + '" target="_blank" >Смотреть вызов</a>'},
            {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#image',
            // Своё изображение иконки метки.
            iconImageHref: '/static/police.png',
            // Размеры метки.
            iconImageSize: [40, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-20, -35]
            });
            //{ preset: 'islands#blueDotIcon' });
        // Размещение геообъекта на карте.
        myMap.geoObjects.add(myGeoObject);
    }
    for (var p in fire)
    {
        // Создание метки.
        var myGeoObject = new ymaps.Placemark(fire[p][0], // координаты точки
            { balloonContent: '<a href="/calls/' + fire[p][1].toString() + '" target="_blank" >Смотреть вызов</a>'},
            {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#image',
            // Своё изображение иконки метки.
            iconImageHref: '/static/fire.png',
            // Размеры метки.
            iconImageSize: [50, 50],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-25, -45]
            });
            //{ preset: 'islands#redDotIcon' });
        // Размещение геообъекта на карте.
        myMap.geoObjects.add(myGeoObject);
    }
    for (var p in amb)
    {
        // Создание метки.
        var myGeoObject = new ymaps.Placemark(amb[p][0], // координаты точки
            { balloonContent: '<a href="/calls/' + amb[p][1].toString() + '" target="_blank" >Смотреть вызов</a>'},
            //{ preset: 'islands#greenDotIcon' });
            {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#image',
            // Своё изображение иконки метки.
            iconImageHref: '/static/amb.png',
            // Размеры метки.
            iconImageSize: [40, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-20, -35]
            });
        // Размещение геообъекта на карте.
        myMap.geoObjects.add(myGeoObject);
    }
    myMap.controls.remove('fullscreenControl');
    myMap.controls.remove('trafficControl');
    myMap.setBounds(myMap.geoObjects.getBounds());
}


