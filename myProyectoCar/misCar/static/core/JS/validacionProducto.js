function validarNombre(){
    var nom=document.getElementById("txtNombre").value;
    if(nom.length < 3 || nom.length > 120){
        alert("el nombre debe tener entre 3 y 120 carcateres");
        return false;
    }
    return true;
}

function validarPrecio(){
    var valor = document.getElementById("txtvalor").value;
    if (valor<1){
        alert("El precio mínimo de un artículo debe ser $1");
        return false;
    }
    return true;
}



function espacios(){
    var espacio_blanco    = /[a-z]/i;  //Expresión regular
    var nombre = document.getElementById("txtNombre").value; 

    if(!espacio_blanco.test(nombre) )
    {
        alert("No se admiten espacio en blanco en el nombre.");
        return false;
    }
    return true;
}



function validarTodo(){
    var r;
    r=validarNombre();
    if(r==false){
        return false;
    }

    r=validarPrecio();
    if(r==false){
        return false;
    }

    r=espacios();
    if(r==false){
        return false;
    }

    return true;
}