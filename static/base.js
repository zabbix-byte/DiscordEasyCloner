function getLog() {
    $.ajax({
        url: 'info.log',
        dataType: 'text',
        success: function (text) {
            words = text.split("\n")
            $("#log").empty()

            if (!text.includes('Websocket closed') && !text.includes('Token Problems') && !text.includes('Target id not exists') && !text.includes('Destination id not exists') && text.length > 0) {
                $("#loading-sec-123").show();
                $("#submit-button").addClass('disabled');
            } else {
                $("#loading-sec-123").hide();
                $("#submit-button").removeClass('disabled');
            }

            if (text.includes('Token Problems')) {
                $("#token").addClass("is-invalid");
            } else {
                $("#token").removeClass("is-invalid");
            }

            if (text.includes('Target id not exists')) {
                $("#target").addClass("is-invalid");
            } else {
                $("#target").removeClass("is-invalid");
            }

            if (text.includes('Destination id not exists')) {
                $("#destination").addClass("is-invalid");
            } else {
                $("#destination").removeClass("is-invalid");
            }


            for (let i = 0; i < words.length; i++) {

                if (!words[i].includes('Shard ID')) {
                    if (words[i].includes('[INFO]')) {
                        $("#log").append(`<p style="color: #4486D5;">` + words[i] + `</p>`);
                    }
                }


            }
            setTimeout(getLog, 1000);

        }
    })
}

function cleanLogs() {
    $("#loading-sec-123").show();
    $("#submit-button").addClass('disabled');
    $("#token").removeClass("is-invalid");
    file_put_contents('info.log', '');
}

$(document).ready(function () {
    getLog();
})
