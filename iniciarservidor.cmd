echo off
color 30
echo 			==================================
echo 			=                                =
echo 			=     SERVIDOR DE PAGINA WEB     =
echo 			=                                =
echo 			=   [ POR FAVOR NO CERRAR!!!! ]  =
echo 			=                                =
echo 			==================================
echo.
echo.

cd C:\MY_ENVS\buro-de-credito\Scripts
activate
cd C:\Users\Admin\Documents\GitHub\buro-de-credito
python manage.py runserver 0.0.0.0:8000
