const productDelete = document.getElementById('Product_delete');
if(productDelete){
  productDelete.addEventListener('click', function () { alert('상품삭제가 완료되었습니다.'); })
}

const productEdit = document.getElementById('Product_edit');
if(productEdit){
  productEdit.addEventListener('click', function () { alert('상품수정이 완료되었습니다.'); })
}

const productNew = document.getElementById('Product_new');
if(productNew){
  productNew.addEventListener('click', function () { alert('상품등록이 완료되었습니다.'); })
}