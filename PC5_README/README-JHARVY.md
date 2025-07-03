## Cambios realizados en la PC5 - Jharvy Cadillo

- Primeramente se modifico el script generate_docs.py para que reciba un parametro, el cual serviria para que genere una carpeta dentro de `docs/` esta carpeta tendria el nombre del tag puesto en el proyecto. Ya que en cada tag habria una actualizacion en la IaC, este seria la manera en que se versione la documentacion de la IaC. Para probar manualmente su funcionamiento. Se tiene que ejecutar el siguiente comando:

    ```bash
    python3 scripts/generate_docs.py --output v1.0.0
    ```

    Este comando crearia la carpeta `docs/v1.0.0` en el cual se almacenaria la documentacion de la IaC.


- Para que la documentacion se genere de manera automatica en la IaC se añadio un nuevo **job** en el pipeline para que genere la documentacion cada vez que se cree un tag. Se ejecuto el script en actions y utilizo una actions externa (`uses: stefanzweifel/git-auto-commit-action@v6`) para el commit y push de la documentacion agregada en la maquina de ejecucion de github a nuestro repositorio.