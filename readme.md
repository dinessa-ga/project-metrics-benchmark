python -m venv venv

pip install pandas

pip install jupyter

### Activar el ambiente virtual

venv\Scripts\activate

### Desplegar local host para jupyter

jupyter notebook

Al cambiar el nombre del directorio del proyecto hubo problemas al desplegar el cuarderno de jupyter.

Se volvió a crear el ambiente virtual, eliminando el anterior. Nuevamente se instaló jupyter. Las demás librerías desde el cuaderno prueba1.ipynb

Sobre seaborn
[Ver documentación](https://seaborn.pydata.org/installing.html)

Sobre Matplotlib
[Ver documentación](https://matplotlib.org/stable/users/explain/quick_start.html)

Sobre numpy
[Ver documentación](https://numpy.org/es/install/)

### Recuerda que...
El ambiente virtual debe describirse en el archivo .gitignore para que no se suba al repositorio remoto esos archivos, de lo contrario deberás hacer lo siguiente:

git rm -r --cached venv

venv: Es el nombre del archivo de tu ambiente virtual

git add .

git commit -m "Eliminando venv del seguimiento de Git"

git push origin main
