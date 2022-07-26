function Guardar() {
    let email = $("#email").val();
    let password = $("#password").val();
    let username = $("#username").val();
    let color = $("#color").val();
    let edad = $("#edad").val();


    $.ajax({
        url: '/agregar_user',
        type: 'POST',
        dataType: 'text',
        data: {
            email: email,
            password: password,
            username: username,
            color: color,
            edad: edad
        },
        success: function(res) {
            alert(res)

            Datos();

            $("#email").val('');
            $("#password").val('');
            $("#username").val('');
            $("#color").val('');
            $("#edad").val('');
            Contar_Dato();
        }
    })
}

$(document).ready(function() {
    Datos();
    Contar_Dato();

})

function Datos() {
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: './listar_datos',
        success: function(response) {
            console.log(response)
                //alert(response)

            let html = '';
            let i = 0;
            for (i = 0; i < response.length; i++) {
                html += '<tr>' +
                    '<td>' + response[i].id + '</td>' +
                    '<td>' + response[i].email + '</td>' +
                    '<td>' + response[i].password + '</td>' +
                    '<td>' + response[i].username + '</td>' +
                    '<td>' + response[i].color + '</td>' +
                    '<td>' + response[i].edad + '</td>' +
                    '<td><button type="button" class="button btn-danger" onclick="Eliminar(' + response[i].id + ')"><i class="fa-solid fa-trash"></i></button>' +
                    '<button class="button btn-success" onclick="Editar(' + response[i].id + ');"><i class="fa-solid fa-pen-to-square"></i></button></td>'
                '</tr>';
            }
            $('#datos').empty(html)
            $('#datos').append(html);

        }
    })
}

function Eliminar(id) {
    //console.log(id);

    $.ajax({
        url: '/eliminar_user',
        dataType: 'text',
        type: 'POST',
        data: {
            id: id
        },
        success: function(r) {


            alert(r);
            console.log(r);
            Datos();
            Contar_Dato();


        }
    })

}


function Editar(id) {


    console.log(id)
    $.ajax({
        url: './obtener_dato/' + id,
        type: 'GET',
        dataType: 'json',
        success: function(rr) {
            // alert(rr);
            console.log(rr);

            $("#id").val(id);
            $("#email").val(rr.email)
            $("#password").val(rr.password)
            $("#username").val(rr.username);
            $("#color").val(rr.color);
            $("#edad").val(rr.edad);

        }
    })


}


function Actualizar() {
    let id = $("#id").val();
    let email = $("#email").val();
    let password = $("#password").val();
    let username = $("#username").val();
    let color = $("#color").val();
    let edad = $("#edad").val();

    $.ajax({
        url: './actualizar_dato',
        type: 'POST',
        data: {
            id: id,
            email: email,
            password: password,
            username: username,
            color: color,
            edad: edad
        },
        dataType: 'text',
        success: function(result) {
            alert(result)
            Datos();
            $("#id").val('');
            $("#email").val('');
            $("#password").val('');
            $("#username").val('');
            $("#color").val('');
            $("#edad").val('');
        }
    })
}

function Contar_Dato() {
    $.ajax({
        url: '/contar_dato',
        type: 'GET',
        dataType: 'json',
        success: function(res) {

            let i = 0;
            let date = ''

            for (i = 0; i < res.length; i++) {
                date += '<span style="color:white; border:1px solid red; border-radius:100%;font-size:80%;background:red;">' +
                    res[i].cantidad + '</span>';


            }

            $("#cantidad").html(date);



        }
    })
}



function Buscar() {

    let buscar = $("#buscar").val();

    $.ajax({
        url: './buscar',
        type: 'POST',
        dataType: 'json',
        data: {
            buscar: buscar
        },
        success: function(responses) {
            // alert(responses);
            console.log(responses);
            if (responses.length > 0) {
                let html = '';
                let i = 0;
                for (i = 0; i < responses.length; i++) {
                    html += '<tr>' +
                        '<td>' + responses[i].id + '</td>' +
                        '<td>' + responses[i].email + '</td>' +
                        '<td>' + responses[i].password + '</td>' +
                        '<td>' + responses[i].username + '</td>' +
                        '<td>' + responses[i].color + '</td>' +
                        '<td>' + responses[i].edad + '</td>' +
                        '<td><button type="button" class="button btn-danger" onclick="Eliminar(' + responses[i].id + ')"><i class="fa-solid fa-trash"></i></button>' +
                        '<button class="button btn-success" onclick="Editar(' + responses[i].id + ');"><i class="fa-solid fa-pen-to-square"></i></button></td>'
                    '</tr>';
                }
                $('#datos').empty(html)
                $('#datos').append(html);

            } else {
                //alert('No se encontraron datos');
                html1 = '<tr><td>No se encontraron datos</td></tr>';

                $('#datos').append(html1);
            }
        }
    })
}