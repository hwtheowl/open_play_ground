(function(){
    var Event = {
        getContents: function(){
            $('button.search').on('click', function(){
                var addr = $('.input-address').val();
                var url = 'https://apis.zigbang.com/v2/search?leaseYn=N&q=';
                    url = url + addr + '&serviceType=원룸';
                console.log(url);
                $.getJSON(url, function(response){
                    console.log(response.items);
                    var tag = '';
                    for(var i = 0; i < response.items.length; i++){
                        console.log(response.items[i])
                        tag += '<tr>';
                        tag += '    <td>' + (i + 1) + '</td>';
                        tag += '    <td>' + items.id + '</td>';
                        tag += '    <td>' + items.name + '</td>';
                        tag += '    <td>' + (Math.round(Number(items.lat) * 100) / 100) + '</td>';
                        tag += '    <td>' + (Math.round(Number(items.lng) * 100) / 100) + '</td>';
                        tag += '    <td>' + items.description + '</td>';
                        tag += '</tr>';
                    };
                    $('.table-wrap>table>tbody').html(tag);
                    $('.table-wrap').show(200);
                });
            });
        }
    };
    Event.getContents();
})();