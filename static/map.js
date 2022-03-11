var myMap;

ymaps.ready(init);

function init()
{
    myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 10
    });
    for (var p in calls)
    {
        // Создание метки.
        var myGeoObject = new ymaps.Placemark(calls[p][0], // координаты точки
            { balloonContent: calls[p][1] > 0 ? '<a href="/calls/' + calls[p][1].toString() + '" target="_blank" >Смотреть вызов</a>' : ''},
            {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#image',
            // Своё изображение иконки метки.
           // iconImageHref: '/static/police.png',
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

    myMap.controls.remove('fullscreenControl');
    myMap.controls.remove('trafficControl');
    myMap.setBounds(myMap.geoObjects.getBounds());
}


