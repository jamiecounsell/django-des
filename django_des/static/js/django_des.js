function stop_event(e) {
    e.stopPropagation();
    e.preventDefault();
}

document.addEventListener("DOMContentLoaded", function(event) {
    var input = document.getElementById('django_des--test-input');
    var form = document.getElementById('django_des--test-form');
    var button = document.getElementById('django_des--test-button');

    input.addEventListener('click', function(e){
        stop_event(e);
    });
});
