// 모두 체크
function allCheck() {
    if($("[name=chkAll]").prop("checked")) {
        $("[name=chk]").prop("checked",true);
    } else {
        $("input[type=checkbox]").prop("checked", false);
    }
}

// 체크
function oneCheck(a)
{
var allChkBox = $("[name=chkAll]");
var chkBoxName = $(a).attr("name");

if( $(a).prop("checked") )
{
    //전체체크박스 수(모두동의하기 체크박스 제외)
    checkBoxLength = $("[name="+ chkBoxName +"]").length;

    //체크된 체크박스 수
    checkedLength = $("[name="+ chkBoxName +"]:checked").length;

    //전체체크박스수 == 체크된 체크박스 수 같다면 모두체크
    if( checkBoxLength == checkedLength ) {
        allChkBox.prop("checked", true);

    } else {
        allChkBox.prop("checked", false);
    }
} else
  {
       allChkBox.prop("checked", false);
  }

}


$(function(){
// 모두 동의하기 체크박스 클릭 시
$("[name=chkAll]").click(function(){
    allCheck(this);
});
// 다른 체크박스 클릭 시
$("[name=chk]").each(function(){
    $(this).click(function(){
        oneCheck(this);
    });
});
});

// 필수정보 확인
var nextBtn = document.getElementById("nextBtn");
var mustchk1 = document.getElementById("mustchk1");
var mustchk2 = document.getElementById("mustchk2");
var mustchk3 = document.getElementById("mustchk3");
nextBtn.addEventListener("click", checkRight);
function checkRight() {
    if(mustchk1.checked==true && mustchk2.checked==true && mustchk3.checked==true) {
        // 어떻게 처리할지 모르겠음...
        return
    } else {
        // 왜 안뜨는가...
        // alert("필수정보를 확인해주세요!");
        confirm("2018년에 이루고자 하는 것들을 이루셨나요?");
    }
}