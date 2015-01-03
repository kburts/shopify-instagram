(function () {
    // Initialize gallery, by finding shopify-instagram-gallery div id.
    function init() {
        $('#shopify-instagram-gallery').append('<input id="instagram-tag-box"></input><button id="update-gallery-tag">update tag</button>');
        $('#shopify-instagram-gallery').append('<div id="instagram-gallery-tag"></div>');
        $('#shopify-instagram-gallery').append('<div id="instagram-gallery-photos"></div');


        $("#update-gallery-tag").bind("click", function () {
            fetchGallery($('#instagram-tag-box').val());
        });
    }

    // AJAX call to create new instagram gallery.
    function createGallery(tag) {
        var api_url = 'https://www.kevinsapps.com/api/gallerycreate/';
        var data = {
            'tag': tag
        };
        console.log('tag: ' + tag);
        $.ajax({
            url: api_url,
            type: 'POST',
            data: JSON.stringify(data),
            headers: {
                'content-type': 'application/json'
            },

            success: function (response) {
                console.log(response);
                console.log('created gallery: ' + response.tag);
                fetchGallery(response.tag);
            },
            error: function (response) {
                console.log('error creating gallery!');
                console.log(response);
            }
        });
    }


    // AJAX call to server to get photos
    function fetchGallery(tag) {
        var api_url = 'https://www.kevinsapps.com/api/gallery/' + tag + '/';
        $.ajax({
            url: api_url,
            success: function (response) {
                console.log(response); // server response
                extractImages(response);
            },
            error: function (response) {
                if (response.statusText == 'NOT FOUND') {
                    console.log('could not find gallery, so creating one.');
                    createGallery(tag);
                    //fetchGallery(tag);
                } else {
                    console.log('error finding gallery!');
                    console.log(response);
                }
            }
        });
    }

    function extractImages(response) {
        console.log(response);
        var photos = response.photos;
        $('#instagram-gallery-photos').empty();
        
        for (var i = 0; i < photos.length; i++) {
            to_append = "<a href='" + photos[i].ig_url + "'><img width=175 height=175 src='" + photos[i].photo_url + "'></a>";
            $('#instagram-gallery-photos').append(to_append);
        }
    }


    var tag = 'snow';
    init();
    fetchGallery(tag);
})();