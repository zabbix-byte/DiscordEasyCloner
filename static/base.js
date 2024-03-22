var current_elements = []


function getLog() {
    $.ajax({
        url: 'info.log',
        dataType: 'text',
        success: function (text) {
            words = text.split("\n")
            for (let i = 0; i < words.length; i++) {

                if (!words[i].includes('Shard ID None has connected to Gateway'))
                {
                    if (!current_elements.includes(words[i]))
                    {
                        $("#log").append(`<p style="color: #4486D5;">`+words[i]+`</p>`);
                        current_elements.push(words[i])
                    }
                    
                }
                
            }
            setTimeout(getLog, 5000);
        }
    })
}

function cleanLogs() {
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
    $("#log").empty()
}

$(document).ready(function () {
    getLog();
})
