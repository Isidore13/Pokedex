function openTab(x){
    let contents = document.querySelectorAll(".container");
    let btns = document.querySelectorAll("button");
    for (let i =0; i < contents.length; i++){
        contents[i].style.display = "none";
        btns[i].classList.remove("active");
    }
    contents[x].style.display ="block";
    btns[x].classList.add("active");
}

function scrolltopokemon() {
    var input, filter, div, pokemon, i;
    input = document.getElementById('lookfor');
    filter = input.value.toUpperCase();
    div = document.getElementsByClassName('pokemon-list')[0];
    pokemon = div.getElementsByClassName('pokemon');

    console.log('Filter:', filter);

    for (i = 0; i < pokemon.length; i++) {
        console.log('Pokemon ID:', pokemon[i].id.toUpperCase());

        if (pokemon[i].id.toUpperCase().indexOf(filter) > -1) {
            pokemon[i].scrollIntoView({ behavior: 'smooth', block: 'start' });
            return;
        }
    }
}

        function submitData() {
            var type1 = $('#type1').val();
            var type2 = $('#type2').val();

            $.ajax({
                url: 'http://localhost:8000/submit',
                type: 'POST',
                data: {type1: type1, type2: type2},
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }

openTab(0)