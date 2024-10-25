document.getElementById('reg_form').addEventListener('submit', GetInput);

valid_el = document.createElement('p');

    function GetInput(event) {
        event.PreventDefault();
        el.appendChild(valid_el);
        var el = document.getElementById('reg_form')
        if (el.log.value === "") {
            valid_el.innerHTML=""

        }
        
    };