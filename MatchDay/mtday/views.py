from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Clubs, User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
        

def home(request):
    # GET 요청에서 'ctprvn_nm', 'signgu_nm', 'item_nm' 값을 가져옴
    ctprvn_nm = request.GET.get('ctprvn_nm') or request.session.get('city')  # 시도명: GET 또는 세션 값
    signgu_nm = request.GET.get('signgu_nm') or request.session.get('district')  # 시군구명: GET 또는 세션 값
    item_nm = request.GET.get('item_nm')
    
    # 초기화된 queryset: 필터링 안 한 전체 데이터
    clubs = Clubs.objects.all()

    # 만약 검색어가 입력되면 해당 필드로 필터링
    if ctprvn_nm:
        clubs = clubs.filter(ctprvn_nm__icontains=ctprvn_nm)  # 시도명 필터
    if signgu_nm:
        clubs = clubs.filter(signgu_nm__icontains=signgu_nm)  # 시군구명 필터
    if item_nm:
        clubs = clubs.filter(item_nm=item_nm)  # 종목명 정확히 일치 필터

    # 모든 종목명 가져오기 (중복 제거)
    sports = Clubs.objects.values_list('item_nm', flat=True).distinct().order_by('item_nm')
    
    return render(request, 'home.html', {
        'clubs': clubs,
        'sports': sports
    })
    
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 세션에 로그인 상태 저장
        print("입력된 username:", username)
        print("입력된 password:", password)

        # 데이터베이스에서 유저 검증
        try:
            user = User.objects.get(username=username, password=password)
            print("로그인 성공: ", user)
            # 세션 설정
            request.session["user_id"] = user.id
            request.session["username"] = user.username
            request.session["city"] = user.city  # 시도명
            request.session["district"] = user.district
            
            messages.success(request, "로그인에 성공했습니다.")
            return redirect("home")  # 로그인 성공 시 홈 페이지로 리디렉션
        except User.DoesNotExist:
            print("로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.")
            messages.error(request, "아이디 또는 비밀번호가 잘못되었습니다.")
    
    return render(request, "login.html")



def sign_up_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        birth_date = request.POST.get('birth_date')
        email = request.POST.get('email')
        city = request.POST.get('region')  # 'region'과 'district'는 템플릿의 select input 이름과 일치해야 함
        district = request.POST.get('district')
        if User.objects.filter(username=username).exists():
            return render(request, 'sign_up.html', {
                'error': '이미 사용 중인 아이디입니다.'
            })

        try:
            user = User.objects.create(
                username=username,
                password=password,
                name=name,
                birth_date=birth_date,
                email=email,
                city=city,
                district=district
            )
            return redirect('login')  # 로그인 페이지로 리디렉션
        except IntegrityError:
            return render(request, 'sign_up.html', {
                'error': '회원가입 중 오류가 발생했습니다. 다시 시도해주세요.'
            })

        return redirect('login')  # 가입 후 로그인 페이지로 리디렉션

    return render(request, 'sign_up.html')

def logout_view(request):
    logout(request)
    messages.success(request, "로그아웃되었습니다.")
    return redirect('login')

from django.contrib.auth.decorators import login_required

def mypage_view(request):
    user_id = request.session.get('user_id')  # 세션에서 사용자 ID 가져오기
    if not user_id:  # 로그인하지 않은 경우
        return redirect('login')

    # 세션에 저장된 사용자 ID로 사용자 정보 가져오기
    user = User.objects.get(id=user_id)
    context = {
        'name': user.name,
        'user_id': user.username,
        'password': user.password,
        'email': user.email,
        'region': user.city,
        'district' : user.district,
        'birth_date': user.birth_date,
    }
    return render(request, 'mypage.html', context)


def edit_mypage_view(request):
    # 개인정보 수정 페이지로 연결
    return render(request, 'edit_mypage.html')

def local_club_list_view(request):
    # 동동랭 섹션에 대한 상세 정보를 보여주는 새로운 페이지
    return render(request, 'local_club_list.html')

def sports_view(request):
    # 추가 섹션 1에 대한 상세 정보를 보여주는 새로운 페이지
    return render(request, 'sports.html')

def board_view(request):
    # 추가 섹션 2에 대한 상세 정보를 보여주는 새로운 페이지
    return render(request, 'board.html')