# ui-test
Приветствую на страничке зачётного приключения

Задание состоит в написании несложного приложения с графическим пользовательским интерфейсом вместе с обвязкой для его использования, тестирования, распространения. Платформа любая, язык любой, тулкит любой

Результат решения задачи надо сдать посредством создания (одного) Pull Request (PR) в этом репозитории. Всё связанное с решением должно лежать в директории с фамилией и инициалами (кроме `.gitmodules`, при их использовании)

На подачу PR действует жёсткий дедлайн; время на выполнение задания ограничено 2 часами (PR, коммиты поданные после 20:03:00 14.02.2024 оцениваться не будут)

Основные требования:
1. Нужно выбрать и указать в сопровождающем файле платформу, под которую реализуется проект; на этой платформе будет производиться его проверка
1. Программа должна быть переносима (её запуск не должен вызывать непреодолимых трудностей на других машинах)
1. При использовании компилируемого языка программирования, решение должно сопровождаться рецептами для сборки (cmake, meson, gradle, ...). При использовании языка программирования, экосистема которого содержит способ распространения пакетов (pip, cargo, ...), реализованная программа должна быть готова к установке посредством этого инструмента
1. Используемый сторонний код (библиотеки, модули и т.п.) должны обеспечиваться либо через специфичный экосистеме менеджер пакетов, либо через git submodules
1. Вместе с кодом сдаётся текстовое пояснение к установке, запуску и тестированию программы (на другой машине)
1. (если используемый язык допускает наследование) программа должна содержать не менее 2 виджетов, полученных путём наследования виджетов тулкита
1. Программа должна соответствовать обозначенным в разделе с датой идее и персональному датасету 

Результат проверки и решение об отметке будет принято в течение следующего за сдачей рабочего дня

## 20240214
Напишите, пожалуйста, программу для отображения данных в графическом интерфейсе через иерархический список
+ За загрузку (18:15, из интернет) датасета отвечает пользователь, из `README.md` должно следовать, по какому пути программа будет его ожидать
+ Можно, но нежелательно, отображать только часть имеющихся полей. В этом случае у пользователя должна быть возможность увидеть не менее двух уровней иерархии представляемых данных
+ При чрезмерной длине датасета, можно ограничиться отображением какой-то разумной её части
+ Выход из программы должен быть реализован через диалоговое окно с подтверждением
+ Язык интерфейса - русский

buj_at https://corgis-edu.github.io/corgis/json/smoking/  
gordeev_an https://corgis-edu.github.io/corgis/json/video_games/  
goryagin_da https://corgis-edu.github.io/corgis/json/coffee/  
ishmanov_tf https://corgis-edu.github.io/corgis/json/covid/  
kiselev_vg https://corgis-edu.github.io/corgis/json/tate/  
kostitsyina_ad https://corgis-edu.github.io/corgis/json/nuclear_explosions/  
markushina_la https://corgis-edu.github.io/corgis/json/earthquakes/  
polyakova_kp https://corgis-edu.github.io/corgis/json/classics/  
sharifullin_af https://corgis-edu.github.io/corgis/json/cars/  
vekovshinin_va https://corgis-edu.github.io/corgis/json/food/  
zvyagina_mo https://corgis-edu.github.io/corgis/json/county_demographics/  

## 20231221
~~Нужно написать специфический (см. персональный макет) калькулятор~~

kostitsyina_ad [mockups/20231221/6.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/6.drawio.svg)  
gordeev_an [mockups/20231221/13.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/13.drawio.svg)  
ishmanov_tf [mockups/20231221/4.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/4.drawio.svg)  
goryagin_da [mockups/20231221/2.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/2.drawio.svg)  
sharifullin_af [mockups/20231221/10.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/10.drawio.svg)  
ragrin_dr [mockups/20231221/8.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/8.drawio.svg) 🏆  
shanturov_mv [mockups/20231221/11.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/11.drawio.svg) 🏆  
kiselev_vg [mockups/20231221/7.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/7.drawio.svg)  
buj_at [mockups/20231221/3.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/3.drawio.svg)  
zvyagina_mo [mockups/20231221/12.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/12.drawio.svg)  
polyakova_kp [mockups/20231221/1.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/1.drawio.svg)  
markushina_la [mockups/20231221/9.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/9.drawio.svg)  
vekovshinin_va [mockups/20231221/5.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/20231221/5.drawio.svg)  
