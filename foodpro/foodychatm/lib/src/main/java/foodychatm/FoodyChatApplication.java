package foodychatm;

@SpringBootApplication
public class FoodyChatApplication {
	public static void main(String[] args) {
        SpringApplication.run(FoodyChatApplication.class, args);

	}

}
@Controller
class FoodyChatController {

    @GetMapping("/")
    public String home() {
        return "home";
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @GetMapping("/signup")
    public String signup() {
        return "signup";
    }

    @GetMapping("/mypage")
    public String mypage() {
        return "mypage";
    }

    @GetMapping("/chatbot")
    public String chatbot() {
        return "chatbot";
    }

    @GetMapping("/image_upload")
    public String imageUpload() {
        return "image_upload";
    }
}

// HTML 파일 경로: src/main/resources/templates

/*
home.html:
<!DOCTYPE html>
<html>
<head><title>FoodyChat Home</title></head>
<body>
<h1>환영합니다! FoodyChat 메인 페이지입니다.</h1>
<a href="/login">로그인</a> | <a href="/signup">회원가입</a>
<a href="/chatbot">AI 챗봇</a> | <a href="/image_upload">이미지 업로드</a>
</body>
</html>

login.html:
<!DOCTYPE html>
<html>
<head><title>로그인</title></head>
<body>
<h2>로그인 페이지</h2>
<form action="/login" method="post">
  아이디: <input type="text" name="username"><br>
  비밀번호: <input type="password" name="password"><br>
  <input type="submit" value="로그인">
</form>
</body>
</html>

signup.html:
<!DOCTYPE html>
<html>
<head><title>회원가입</title></head>
<body>
<h2>회원가입 페이지</h2>
<form action="/signup" method="post">
  아이디: <input type="text" name="username"><br>
  비밀번호: <input type="password" name="password"><br>
  비밀번호 확인: <input type="password" name="password_confirm"><br>
  <input type="submit" value="회원가입">
</form>
</body>
</html>

mypage.html:
<!DOCTYPE html>
<html>
<head><title>마이페이지</title></head>
<body>
<h2>마이페이지</h2>
<p>회원 정보를 관리하는 페이지입니다.</p>
</body>
</html>

chatbot.html:
<!DOCTYPE html>
<html>
<head><title>AI 챗봇</title></head>
<body>
<h2>AI 챗봇</h2>
<p>음식 관련 대화를 시작해보세요!</p>
<textarea placeholder="메시지 입력"></textarea>
<button>전송</button>
</body>
</html>

image_upload.html:
<!DOCTYPE html>
<html>
<head><title>이미지 업로드</title></head>
<body>
<h2>이미지 업로드</h2>
<form action="/upload" method="post" enctype="multipart/form-data">
  파일 선택: <input type="file" name="file"><br>
  <input type="submit" value="업로드">
</form>
</body>
</html>
*/
