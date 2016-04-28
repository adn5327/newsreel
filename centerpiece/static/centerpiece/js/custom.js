function curDate(tag, country){
    if(document.getElementById(tag).innerHTML != ''){
        document.getElementById(tag).innerHTML = '';
        return;
    }
    $.ajax({
        type: 'GET',
        url: 'https://restcountries.eu/rest/v1/name/'+country+'?fullText=true',
        dataType: 'json',
        success: function(msg) {
            document.getElementById(tag).innerHTML = 
                '<br><p> Population: '+ msg[0].population +'</p>'+
                '<p> Area: ' + msg[0].area + '</p>' +
                '<p> Capital: '+ msg[0].capital + '</p>' +
                '<p> Region: ' + msg[0].region + '</p>' +
                '<p> Subregion: ' + msg[0].subregion + '</p>';
                
        }
    });
}

