from rest_framework import serializers
from reservation.models import Reservation
class ReservationSerializer(serializers.ModelSerializer):
    roomtype = serializers.CharField(source='bookedRoomId.roomtype', read_only=True)
    roomNo = serializers.CharField(source='bookedRoomId.roomNo', read_only=True)
    clientFirstName = serializers.CharField(source='personId.firstName', read_only=True)
    clientLastName = serializers.CharField(source='personId.lastName', read_only=True)
   
    class Meta:
        model=Reservation
        fields=('bookingId','bookedRoomId','roomNo','personId','clientFirstName','clientLastName','checkInDate','checkOutDate','bookingDate','paymentTransactionToken','paid','roomtype')