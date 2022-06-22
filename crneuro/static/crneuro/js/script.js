function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const form = document.querySelector('form [name=filter]');

form.addEventListener('submit', function(e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.tab-content>.row');
    div.innerHTML = output;
}

let html = '\
{{#profile}}\
    <div class="col-md-4">\
    <table class="table table-hover table-bordered">\
  	<tbody>\
		<tr>\
            <td>   </td>\
			<td>{{ id }}</td>\
			<td>{{ fio }}</td>\
			<td>{{ position }}</td>\
			<td>{{ phone }}</td>\
            <td>Рабочий</td>\
        </tr>\
	</tbody>\
 </table>\
{{/profile}}'


