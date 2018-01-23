SDS 2 (Django Message Board) Tutorial

## Add git clone here

## Add show basic functiality here `python manage.py migrate` and `python manage.py createsuperuser` (`python manage.py runserver`)

1. Create new page for editing a message.
    1. This begins with setting up a route in board/urls.py.
	    1. Add `path(r'edit/<int:msg_id>/', views.edit_msg, name='edit_msg'),` to
		   the `urlpatterns = [...]` list.
		2. This directs a route of the form **"http://localhost:8000/edit/10/"**
		   which will send the user to a edit page for the message with id 10.
	2. Create view method (the C, Controller, in the MVC format) in board/views.py,
	   called `edit_msg` as specified in the url route "`views.edit_msg`".
	    1. The function will be `def edit_msg(request, msg_id)`.  This takes the
		   request object and the msg_id, from the url, as the parameters.
		2. The total function definition is:
		```python
		def edit_msg(request, msg_id):
			message = Message.objects.filter(id=msg_id).first()

			if message is None:
				return HttpResponseForbidden("This message doesn't exist.")
			else:
				msg_form = NewMessageForm(request.POST or None, instance=message)

				if msg_form.is_valid():
					msg_form.save()
					return redirect(reverse('index'))
				
			return render(request, 'edit.html', {
				'msg_form': msg_form,
				'message': message,
			})
		```
		3. Create the **board/template/edit.html** template.
		```html
		{% extends 'base.html' %}

		{% block content %}

		<div class='text-center'>
			<br/>
			<h4>Edit Message</h4>
			<br/>
		</div>

		<form class="form-group" id="message-post" method="POST" action="{% url 'edit_msg' message.id %}">

			{% csrf_token %}

			<div class="row">
				<div class="col-md-12" align="center">
					<p id="errors" class="text-center">
						{{ msg_form.text.errors.as_text }}
					</p>
				</div>
			</div>

			<div class="row">
				<div class="input-group">
					{{ msg_form.text }}
					<input type="submit" value="Submit">
				</div>
			</div>

		</form>
			
		{% endblock %}
		```
	3. Create edit button for each message in **board/template/index.html**
		1. Find the table where the messages are being added, sepcifally find the line
		   `<td>{{ m.text }}</td>` and add right below it
		   `<td><a class="button float-right" href="{% url 'edit_msg' m.id %}">Edit</a></td>`
	4. Show off functionality
	
2. Add temp user name text fields to main page (required), makemigrations, migrate, update index.html, (and for advanced update edit page)
		