function request_async(){
    // 使用fetch()函数进行异步请求如果服务端响应速度极慢则不会阻塞页面
    fetch('/api/v1/test').then(
        response => response.text()
    ).then(
        text => {
            document.getElementById('fast_test_example_text').innerText = text
        }
    )
}
