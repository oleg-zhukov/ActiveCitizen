# all categories
сategories = [1, 2, 3, 66, 78, 89, 2201]

# all themes
themes = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
          19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 41, 42, 43, 44, 47, 49, 50, 52, 53, 59, 60, 61, 63,
          64]

# id: name of theme
translateT = {1: 'Нечитаемые/поврежденные дорожные знаки',
              11: 'Наличие опасно выступающих элементов над покрытиями (дорожными, тротуарными и т.д.), таких как арматура, бетонные блоки и т.п.',
              12: 'Ямы, выбоины, выступы на дорогах',
              14: 'Подтопление проезжей части',
              15: 'Открытый (просевший) люк или ливневка на дороге',
              19: 'Реклама на тротуаре вдоль дорог',
              2: 'Противоречия при установке дорожных знаков / разметки / светофора, неправильно установленные дорожные знаки / разметка / светофор',
              21: 'Неисправность/недоступность инфраструктуры для маломобильных граждан / колясок на дорогах',
              22: 'Неисправное освещение на дорогах',
              23: 'Грязь, мусор, разрушение стен и покрытия в подземных и надземных пешеходных переходах',
              24: 'Мусор, свалки у обочин дорог, на тротуаре, газоне',
              3: 'Стертая дорожная разметка',
              32: 'Нескошенная трава вдоль тротуаров и обочин дорог',
              35: 'Некачественный уход за деревьями, кустарниками вдоль дорог, тротуаров (кронирование, вырубка сухостоев, ликвидация аварийных деревьев)',
              39: 'Неубранный снег, гололёд на проезжей части, тротуаре',
              41: 'Снеговые кучи на обочинах дорог, тротуаре',
              64: 'Брошенный разукомплектованный автомобиль на проезжей части',
              8: 'Неисправный светофор', 9: 'Повреждение дорожного ограждения',
              13: 'Ямы, выбоины, выступы на придомовой территории',
              16: 'Открытый (просевший) люк или ливневка во дворе',
              18: 'Реклама на тротуаре во дворах',
              20: 'Неисправность/недоступность инфраструктуры для маломобильных граждан / колясок во дворе',
              25: 'Мусор на придомовой территории',
              26: 'Нарушение графика вывоза мусора с контейнерной площадки во дворе',
              27: 'Несвоевременная уборка территории контейнерной площадки во дворе',
              30: 'Вытоптанный, заезженный газон',
              31: 'Нескошенная трава на придомовой территории',
              37: 'Некачественный уход за деревьями, кустарниками на придомовой территории (кронирование, вырубка сухостоев, ликвидация аварийных деревьев) во дворах',
              38: 'Брошенный разукомплектованный автомобиль на проезжей части, во дворе',
              42: 'Неубранный снег, гололед во дворе',
              43: 'Снег, сосульки на крыше дома',
              44: 'Снег, наледь на входных группах, перилах',
              5: 'Неисправное освещение во дворах',
              28: 'Скопление мусора в парках, скверах',
              33: 'Нескошенная трава вдоль пешеходных дорожек с твердым покрытием в парках',
              34: 'Ямы, выбоины, выступы на пешеходных дорожках или тротуарах',
              36: 'Некачественный уход за деревьями, кустарниками вдоль пешеходных дорожек, тротуаров в парках',
              47: 'Неубранный снег, наледь на пешеходных дорожках, тротуаре',
              6: 'Неисправное освещение в парках',
              17: 'Реклама на тротуаре',
              10: 'Повреждения остановочного павильона',
              29: 'Грязь, мусор на остановке',
              49: 'Неубранный снег, наледь на остановке',
              59: 'Неудовлетворительное санитарное состояние транспортного средства',
              60: 'Отказ водителей принимать банковские карты в качестве оплаты за проезд',
              61: 'Несоблюдение маршрута',
              63: 'Некорректное поведение водителя/кондуктора',
              4: 'Неисправное уличное освещение в общественных местах',
              50: 'Проблемы при получении социальной помощи',
              52: 'Проблемы при получении социальной помощи ',
              53: 'Проблемы при получении социальной помощи'}
# id: name of categorie
translateC = {1: 'Дороги',
              2: 'Дворы',
              3: 'Парки и общественные территории',
              66: 'Рекламные конструкции',
              78: 'Общественный транспорт',
              89: 'Уличное освещение',
              2201: 'Социальная помощь'}

# id of theme: id of categorie
themeToCat = {1: 1,
              2: 1,
              3: 1,
              4: 89,
              5: 2,
              6: 3,
              8: 1,
              9: 1,
              10: 78,
              11: 1,
              12: 1,
              13: 2,
              14: 1,
              15: 1,
              16: 2,
              17: 66,
              18: 2,
              19: 1,
              20: 2,
              21: 1,
              22: 1,
              23: 1,
              24: 1,
              25: 2,
              26: 2,
              27: 2,
              28: 3,
              29: 78,
              30: 2,
              31: 2,
              32: 1,
              33: 3,
              34: 3,
              35: 1,
              36: 3,
              37: 2,
              38: 2,
              39: 1,
              41: 1,
              42: 2,
              43: 2,
              44: 2,
              47: 3,
              49: 78,
              50: 2201,
              52: 2201,
              53: 2201,
              59: 78,
              60: 78,
              61: 78,
              63: 78,
              64: 1}

# id of categorie: ids of themes
catToThemes = {
    1: [1, 11, 12, 14, 15, 19, 2, 21, 22, 23, 24, 3, 32, 35, 39, 41, 64, 8, 9],
    2: [13, 16, 18, 20, 25, 26, 27, 30, 31, 37, 38, 42, 43, 44, 5],
    3: [28, 33, 34, 36, 47, 6],
    66: [17],
    78: [10, 29, 49, 59, 60, 61, 63],
    89: [4],
    2201: [50, 52, 53]
}
from tables import *
for i in catToThemes[78]:
    print(themes.index(i))