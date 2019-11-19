from django.shortcuts import render, render_to_response
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def MainFunc(request):
    return render_to_response('main.html')

def ListFunc(request):
    '''
    sql = "select * from sangdata"
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    '''
    #datas = Sangdata.objects.all()
    #return render(request, 'list.html', {'sangpums':datas})
    
    # ---------페이지 나누기---------
    datas = Sangdata.objects.all().order_by('-code') # 코드별 decs
    paginator = Paginator(datas, 3)  # 페이지 당 3행씩 출력하려고 함
    try:                            # 페이지가 3으로 딱 나누어지지 않을 경우 대비
        page = request.GET.get('page')
    except:
        page = 1   # client에서 페이지 번호가 안 넘어오면 초기값으로 1을 줌
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:  # 페이지가 정수가 아닌 경우
        data = paginator.page(1)
    except EmptyPage:  # 페이지가 받아지지 않은 경우
        data = paginator.page(paginator.num_pages())
        
    # 개별 페이지 표시용 작업
    allpage = range(paginator.num_pages + 1)
    #print(allpage)
    
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})  # 페이징 처리는 list2를 사용
    
def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        Sangdata(                               # Sangdata는 model의 데이터
            code = request.POST.get("code"),
            sang = request.POST.get("sang"),
            su = request.POST.get("su"),
            dan = request.POST.get("dan"),
        ).save()
        
    #print(code, sang)
    return HttpResponseRedirect('/sangpum/list')

def UpdateFunc(request):
    #print(request.GET.get('code')) # 값이 넘어오는지 보는법
    data = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'sang_one':data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code')) # 수정할 자료를 읽어온다(받는다)
        upRec.code = request.POST.get('code') # 값을 입력
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save()
        
    return HttpResponseRedirect('/sangpum/list') # 수정 후 상품보기

def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete() # 해당 아이디의 자료를 삭제
   
    return HttpResponseRedirect('/sangpum/list') # 삭제 후 상품보기