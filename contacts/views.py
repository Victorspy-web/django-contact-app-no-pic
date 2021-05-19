from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Contact


class ContactList(LoginRequiredMixin, ListView):
	model = Contact
	template_name = 'contacts/index.html'
	context_object_name = 'contacts'

	# This code below makes each user see what belongs to them
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["contacts"] = context['contacts'].filter(user=self.request.user)
		context["count"] = context['contacts'].filter().count()

		# To search things we have in our database
		search_input = self.request.GET.get('search-area') or ''
		if search_input:
			context['contacts'] = context['contacts'].filter(name__icontains=search_input)

		context['search_input'] = search_input

		return context


# CREATE
@login_required(login_url='login')
def contact_create(request):
	if request.method == "POST":
		user = request.user
		name = request.POST['fullname']
		group = request.POST['group']
		number = request.POST['phone-number']
		email = request.POST['e-mail']
		address = request.POST['address']
		note = request.POST['note']

		contact = Contact(
			user=user,
			name=name,
			group=group,
			number=number,
			email=email,
			address=address,
			note=note
		)

		contact.save()
		return redirect('home')

	return render(request, 'contacts/create.html')


# READ
@login_required(login_url='login')
def contact(request, pk):
	contact = Contact.objects.get(id=pk)

	context = {
		'contact': contact,
	}

	return render(request, 'contacts/contact-profile.html', context)


# UPDATE
@login_required(login_url='login')
def update_contact(request, pk):
	contact = Contact.objects.get(id=pk)

	if request.method == "POST":
		contact.name = request.POST['fullname']
		contact.group = request.POST['group']
		contact.number = request.POST['phone-number']
		contact.email = request.POST['e-mail']
		contact.address = request.POST['address']
		contact.note = request.POST['note']

		contact.save()
		return redirect('home')

	context = {
		'contact': contact
	}

	return render(request, 'contacts/edit.html', context)


# DELETE
@login_required(login_url='login')
def delete_contact(request, pk):
	contact = Contact.objects.get(id=pk)

	if request.method == "POST":
		contact.delete()
		return redirect('home')

	context = {
		'contact': contact
	}
	return render(request, 'contacts/delete.html', context)
