from django.db import models
# Create your models here.

from django.db import models

from account.models import CustomUser
from file.models import File
from project.validators import validate_version_format

STATUS_CHOICE = [('RET', '반려'),
                 ('SUC', '성공'),
                 ('RDY', '검사전')]

PHASE_CHOICE = [
    ('BD', '입찰'),  # Bid
    ('PP', '개발준비'),  # Prepare
    ('AN', '분석'),  # Analysis
    ('DE', '설계'),  # design
    ('TE', '테스트'),  # Test
    ('IM', '전개'),  # Implementation
    ('TO', '인도')]  # Take over

ACTIVITY_CHOICE = [
    ('BD10', 'RFP 작성'),
    ('BD20', '제안서 작성'),
    ('BD30', '과업 범위 협상'),
    ('BD40', 'WBS 및 과업수행계획서 작성'),
    ('PP10', 'TFT구성 및 테일러링'),
    ('PP20', '개발 사전준비'),
    ('AN10', '분석 단계 테일러링'),
    ('AN20', '요구사항 분석'),
    ('AN30', '업무/데이터분석'),
    ('AN40', '아키텍처분석'),
    ('AN50', '분석단계 테스트계획'),
    ('AN60', '분석단계점검'),
    ('DE10', '설계단계 테일러링'),
    ('DE20', '아키텍처설계'),
    ('DE30', '어플리케이션설계'),
    ('DE40', 'DB 설계'),
    ('DE50', '데이터전환설계'),
    ('DE60', '설계단계 테스트계획'),
    ('DE70', '설계단계점검'),
    ('C010', '구현단계 테일러링'),
    ('CO20', '구현준비'),
    ('СОЗО', '개발'),
    ('CO40', '단위 테스트'),
    ('CO50', '구현단계점검'),
    ('TE10', '시험단계 테일러링'),
    ('TE20', '테스트'),
    ('TE30', '시험단계점검'),
    ('IM10', '전개단계 테일러링'),
    ('IM20', '리허설'),
    ('IM30', '전개'),
    ('TO10', '인도단계 테일러링'),
    ('TO20', '인수인계'),
    ('TO30', '교육'),
    ('T040', '종료단계점검')]

TASK_CHOICE = [
    ('BD11', 'RFP 확인'),
    ('BD12', '제안서 작성'),
    ('BD13', '과업 범위서 작성'),
    ('BD13', '수행계획서 작성'),
    ('PP11', '사업TFT구성'),
    ('PP12', '방법론 테일러링'),
    ('PP21', '정보화 개발준비'),
    ('AN11', '분석단계 방법론 테일러링'),
    ('AN21', '요구사항수집'),
    ('AN22', '요구사항정의'),
    ('AN23', '유스케이스 기술'),
    ('AN24', '요구사항 추적'),
    ('AN31', '업무 분석'),
    ('AN32', '데이터 분석'),
    ('AN41', '현행아키텍처 분석'),
    ('AN51', '총괄테스트 계획'),
    ('AN61', '분석단계 결과점검'),
    ('DE11', '설계단계 방법론 테일러링'),
    ('DE21', 'SW아키텍처 설계'),
    ('DE22', '시스템 아키텍처 설계'),
    ('DE31', '클래스 설계'),
    ('DE32', '사용자 인터페이스 설계'),
    ('DE33', '컴포넌트 설계'),
    ('DE34', '인터페이스 설계'),
    ('DE35', ' 배치 설계'),
    ('DE36', ' 사용자 웹 구성 설계'),
    ('DE41', ' 개념 DB 설계'),
    ('DE42', ' 논리 DB설계'),
    ('DE43', ' 물리 DB설계'),
    ('DE44', ' 데이터흐름도(DFD)작성'),
    ('DE45', ' 특허데이터검증식(BR)작성'),
    ('DE51', ' 데이터 전환/검증계혹'),
    ('DE52', ' 데이터 정비계획'),
    ('DE61', ' 단위테스트케이스작성'),
    ('DE62', ' 통합테스트시나리오작성'),
    ('DE63', ' 시스템테스트시나리오작성'),
    ('DE64', ' 사용자테스트시나리오작상'),
    ('DE71', ' 설계단계 결과점검'),
    ('C011', ' 구현단계 방법론 테일러르'),
    ('CO21', ' 개발환경 구성'),
    ('CO31', ' 프로그램 개발'),
    ('CO41', ' 단위 테스트'),
    ('CO51', ' 웹표준점검'),
    ('CO52', '소스품질검사'),
    ('CO53', '구현단계 결과점검'),
    ('TE11', '시험단계 방법론 테일러링'),
    ('TE21', '테스트 준비작업'),
    ('TE22', '통합테스트'),
    ('TE23', '사용자테스트'),
    ('TE31', '시험단계 결과물점검'),
    ('IM11', '전개단계 방법론 테일러링'),
    ('IM21', '리허설준비작업'),
    ('IM22', '최종점검 및 리허설'),
    ('IM31', '전개준비작업'),
    ('IM32', '최종점검 및 전개'),
    ('TO11', '인도단계 방법론 테일러링'),
    ('TO21', '인수인계 계획'),
    ('TO22', 'EA 현행화'),
    ('TO23', '매뉴얼 작성'),
    ('TO24', '산출물 현행화'),
    ('TO25', '산출물인수인계'),
    ('T031', '교육준비 및 교육'),
    ('T041', '종료단계 결과점검')]

OUTPUT_CHOICE = [
    ('BD11-1', 'RFP'),
    ('BD12-1', '제안서'),
    ('BD13-1', '과업범위협상서'),
    ('BD14-1', '수행계획서'),
    ('BD14-2', 'WBS'),
    ('PP11-1', 'TFT 구성계획서'),
    ('PP12-1', '방법론테일러링결과서'),
    ('AN11-1', '분석단계 방법론 테일러링 결과서'),
    ('AN21-1', '인터뷰계획서'),
    ('AN21-2', '인터뷰결과서'),
    ('AN22-1', '요구사항정의서'),
    ('AN23-1', '유스케이스명세서'),
    ('AN24-1', '요구사항 추적표'),
    ('AN31-1', '현행비즈니스 프로세스 정의서'),
    ('AN31-2', '현행비즈니스업무흐름도'),
    ('AN31-3', 'To-Be비즈니스프로세스정의서'),
    ('AN31-4', 'To-Be비즈니스업무흐름도'),
    ('AN32-1', '현행데이터분석서'),
    ('AN32-2', '전환대상업무 및 범위정의서'),
    ('AN41-1', '현행 아키텍처 분석서'),
    ('AN51-1', '총괄테스트계획서'),
    ('AN61-1', '분석단계점검 결과서'),
    ('AN61-2', '분석단계점검 조치결과서'),
    ('DE11-1', '설계단계 방법론 테일러링 결과서'),
    ('DE21-1', 'SW아키텍처설계서'),
    ('DE22-1', '시스템아키텍처설계서'),
    ('DE31-1', '클래스설계서'),
    ('DE32-1', '사용자인터페이스설계서'),
    ('DE33-1', '컴포넌트설계서'),
    ('DE34-1', '인터페이스설계서'),
    ('DE35-1', '배치프로그램설계서'),
    ('DE36-1', '사용자인터페이스 웹 구성도'),
    ('DE41-1', '개념데이터모델(ERD)'),
    ('DE42-1', '논리데이터요소정의서'),
    ('DE42-2', '물리데이터요소정의서'),
    ('DE42-3', '논리 물리 엔터티관계 다이어그램'),
    ('DE42-4', '표준데이터사전정의서'),
    ('DE43-1', 'Object 정의서'),
    ('DE43-2', '데이터베이스설계서'),
    ('DE44-1', '데이터흐름도(DFD)'),
    ('DE45-1', '특허데이터검증식(BR)정의서'),
    ('DE51-1', '데이터전환 계획서'),
    ('DE51-2', '데이터 전환 매핑 정의서'),
    ('DE51-3', '데이터전환프로그램명세서'),
    ('DE51-4', '데이터검증프로그램명세'),
    ('DE52-1', '데이터정비 계획서'),
    ('DE61-1', '단위테스트 케이스'),
    ('DE62-1', '통합테스트 시나리오'),
    ('DE63-1', '시스템테스트시나리오'),
    ('DE64-1', '사용자테스트시나리오'),
    ('DE71-1', '설계단계점검 결과서'),
    ('DE71-2', '설계단계점검 조치결과서'),
    ('C011-1', '구현단계 방법론 테일러링 결과서'),
    ('CO21-1', '개발환경 구성 계획서'),
    ('C041-1', '단위테스트 결과서'),
    ('CO51-1', '웹접근성 점검 보고서'),
    ('CO51-2', '웹호환성 점검 보고서'),
    ('CO52-1', '소스품질 검사 보고서'),
    ('CO52-2', '보안약점 진단 결과서'),
    ('C053-1', '구현단계점검 결과서'),
    ('C053-2', '구현단계점검 조치결과서'),
    ('TE11-1', '시험단계 방법론 테일러링 결과서'),
    ('TE22-1', '통합테스트결과서'),
    ('TE23-1', '사용자테스트결과서'),
    ('TE31-1', '시험단계점검 결과서'),
    ('TE31-2', '시험단계점검 조치결과서'),
    ('IM11-1', '전개단계 방법론 테일러링 결과서'),
    ('IM21-1', '리허설 계획서'),
    ('IM22-1', '리허설 체크리스트'),
    ('IM22-2', '리허설 결과서'),
    ('IM22-3', '시스템테스트 결과서(리허설)'),
    ('IM31-1', '전개 계획서'),
    ('IM32-1', '전개 체크리스트'),
    ('IM32-2', '전개 결과서'),
    ('IM32-3', '시스템테스트 결과서(전개)'),
    ('TO11-1', '인도단계 방법론 테일러링 결과서'),
    ('TO23-1', '운영자매뉴얼'),
    ('T023-2', '사용자매뉴얼'),
    ('TO23-3', '기반운영매뉴얼'),
    ('T031-1', '교육참석자명단'),
    ('T041-1', '종료단계점검 결과서'),
    ('T041-2', '종료단계점검 조치결과서')]


class Project(models.Model):
    # 프로젝트 이름
    name = models.CharField(max_length=100)
    # 프로젝트 별명
    alias = models.CharField(max_length=100)
    # 프로젝트 아이디(고유)
    id = models.CharField(max_length=20, primary_key=True)
    # 프로젝트 시작 기간
    start_date = models.DateField()
    # 프로젝트 종료 기간
    end_date = models.DateField()
    # 진척율
    progress_rate = models.FloatField(null=True, default=0)
    # 근무 장소
    location = models.CharField(max_length=100, default='pai')

    def __str__(self):
        return self.id


class ProjectFile(File):
    id = models.CharField(max_length=20, primary_key=True)  # 산출물 고유 아이디
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)  # 프로젝트
    phase = models.CharField(max_length=2, choices=PHASE_CHOICE)  # 산출물 단계 코드
    activity = models.CharField(max_length=4, choices=ACTIVITY_CHOICE)  # 산출물 행동 코드
    task = models.CharField(max_length=4, choices=TASK_CHOICE)  # 산출물 작업 코드
    output = models.CharField(max_length=6, choices=OUTPUT_CHOICE)  # 산출물 코드
    writer = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, related_name='projectfile_writer')  # 작성자 , writer 삭제시 해당 자료에 대한 권한을 넘겨 줘야합니다.
    reviewer = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT,related_name='projectfile_reviewer')  # 검토자 , reviewer 삭제시 해당 자료에 대한 권한을 넘겨 줘야합니다.
    version = models.CharField(max_length=15,validators=[validate_version_format], default='v.0.0.1')  # 버전

    review_date = models.DateTimeField()  # 산출물 검토 기간
    deadline_date = models.DateTimeField()  # 마감 기간
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default='RDY')  # 산출물 승인 상태

    def __str__(self):
        return self.name
