document.getElementById('form').addEventListener('submit', GetFormValue);

function GetFormValue(event) {
    event.preventDefault();
    var el = document.getElementById('form')   
    if (el.log.value == '' || el.email_.value == '' || el.pass.value == '' || el.rep_pass.value == '') {
        el.innerHTML +='<p style = "font-size: 6px; color: #fff;">Введены некорректные данные</p>';
        
    }else{
        el.innerHTML +='<p style = "font-size: 6px; color: #fff;">Введены некорректные данные</p>';
    };   
    
    return false;    
};