document.addEventListener('DOMContentLoaded',() => {
    const elementosCarousel = document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel,{
        duration: 150,
        dist: -80,
        shift:5,
        padding: 5, 
        numVisible: 2,
        indicators: true,
        noWrap: false
    });
});

function validarRut(){
    var rut=document.getElementById("txtRut").value;
    if (rut.length!=10) {
        alert("El rut no tiene el largo necesario");
        return false;
    }
    var num=3;
    var suma=0;
    for (let index = 0; index <8; index++) {
        var carac = rut.slice(index, index + 1);
        suma = suma + (carac * num);
        num=num-1;
        if (num==1) {
            num=7;
        }
    }
    
    var resto= suma%11;
    var dv= 11 - resto;
    
    if (dv > 9) {
        
        if (dv==10) {
            dv='K';
            
        }
        else{
            dv=0;
        }
    }
    
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("Rut incorrecto");
        return false;
    }
    return true;
    
}