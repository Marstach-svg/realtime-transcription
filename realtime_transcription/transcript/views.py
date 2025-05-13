from django.shortcuts import render


#meeting, transcript, (delete, update関係も追加で作成)
def meeting_view(request):
    return render(request, "meeting.html", {"form": form})