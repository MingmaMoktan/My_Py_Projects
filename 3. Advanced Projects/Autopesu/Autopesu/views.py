from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'templates/index.html')

def userform(request):
    if request.method == 'POST':
        try:
            customer_name = request.POST.get('customerName')
            customer_phone = request.POST.get('customerPhone')
            customer_email = request.POST.get('customerEmail')
            car_model = request.POST.get('carModel')
            service_type = request.POST.get('serviceType')
            booking_date = request.POST.get('bookingDate')
            booking_time = request.POST.get('bookingTime')
            additional_notes = request.POST.get('additionalNotes')

            # Example: just display the data for now
            return HttpResponse(f"""
                <h2>Booking Received</h2>
                <p><strong>Name:</strong> {customer_name}</p>
                <p><strong>Phone:</strong> {customer_phone}</p>
                <p><strong>Email:</strong> {customer_email}</p>
                <p><strong>Car Model:</strong> {car_model}</p>
                <p><strong>Service Type:</strong> {service_type}</p>
                <p><strong>Booking Date:</strong> {booking_date}</p>
                <p><strong>Booking Time:</strong> {booking_time}</p>
                <p><strong>Additional Notes:</strong> {additional_notes}</p>
            """)
        except Exception as e:
            # Handle any unexpected error and inform the user
            return HttpResponse(f"<h2>Error</h2><p>There was a problem processing your booking: {str(e)}</p>", status=400)
    return render(request, 'userform.html')