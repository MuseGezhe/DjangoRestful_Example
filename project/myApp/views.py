from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.six import BytesIO
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from myApp.models import Student
from myApp.serializers import StudentSerializer


def index(request):
    return HttpResponse('Hello_restful')

'''
restful风格
数据传输一般均为json格式，因此，得到请求数据我们需要以下步骤：
1.GET请求，（查询数据）直接将查到的数据序列化操作，然后转化为json数据返回
2.POST.PUT.PATCH请求，进行增加、修改操作时，需要先将数据转化为json数据，
然后进行反序列化，再次进行序列化操作保存对象，然后转换为json数据返回
【注意】数据进行反序列化操作，得到是正常的dict，不能进行保存，所以需要序列化
后进行数据保存
流程：得到数据→序列化操作→转换为json格式→进行增删改操作，需要反序列化
→保存数据，需要将数据先序列化才能进行保存→最后转化为json格式返回数据
'''

@api_view(['GET','POST'])
def studentsList(request):
    if request.method == 'GET':
        stus = Student.objects.all()
        # 序列化
        serializer = StudentSerializer(stus,many=True)
        # 转化为json数据响应
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        '''
        # 先将通过表单创建的数据转化为json数据
        content = JSONRenderer().render(request.POST)
        # 将json数据反序列化成正常的字典格式的数据
        stus = BytesIO(content)
        stuDict = JSONParser().parser(stus)
        # 在进行序列化
        serializer = StudentSerializer(data=stuDict)
        '''
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid:
            #进行存储数据
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse({'error':serializer.errors},status=400)


@api_view(["GET",'PUT','DELETE'])
def studentDetail(request,pk):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return JsonResponse({'error':str(e)},status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse({'error':serializer.errors},status=400)
    elif request.method == 'DELETE':
        stu.delete()
        return JsonResponse(status=204,content_type='application/json')