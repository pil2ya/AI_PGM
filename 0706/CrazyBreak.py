import pygame
import sys
import random
import math

# ===== 게임 초기화 =====
pygame.init()
WIDTH, HEIGHT = 640, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🔥 CRAZY BRICK BREAKER 🔥")
clock = pygame.time.Clock()

# ===== 색상 정의 =====
BG_COLOR = (15, 15, 25)
PADDLE_COLOR = (0, 255, 200)
BALL_COLOR = (255, 0, 100)
WHITE = (255, 255, 255)

# ===== 게임 상태 변수 =====
score = 0
lives = 3
combo = 0
combo_timer = 0
game_over = False
game_won = False

# ===== 파티클(파편) 시스템 =====
particles = []

def create_particles(x, y, color):
    """벽돌이 깨질 때 사방으로 튀는 화려한 파편 생성"""
    for _ in range(12):
        particles.append({
            "x": x, "y": y,
            "vx": random.uniform(-4, 4),
            "vy": random.uniform(-4, 4),
            "radius": random.randint(3, 6),
            "color": color,
            "life": 1.0  # 투명도 조절용 수명
        })

def update_particles():
    for p in particles[:]:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["life"] -= 0.04  # 점차 사라짐
        if p["life"] <= 0:
            particles.remove(p)

def draw_particles():
    for p in particles:
        alpha = int(p["life"] * 255)
        # pygame에서 투명도가 적용된 원 그리기
        surf = pygame.Surface((p["radius"]*2, p["radius"]*2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*p["color"], alpha), (p["radius"], p["radius"]), p["radius"])
        screen.blit(surf, (p["x"] - p["radius"], p["y"] - p["radius"]))

# ===== 패들 클래스 =====
class Paddle:
    def __init__(self):
        self.width = 110
        self.height = 16
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        # 마우스 X 좌표를 따라 부드럽게 이동
        mouse_x = pygame.mouse.get_pos()[0]
        self.rect.centerx = mouse_x
        # 화면 밖 이탈 방지
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH

    def draw(self):
        # 둥근 모서리 패들 그리기
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect, border_radius=8)
        # 패들 내부 네온 하이라이트 효과
        pygame.draw.rect(screen, WHITE, self.rect.inflate(-4, -6), border_radius=4)

# ===== 공 클래스 =====
class Ball:
    def __init__(self):
        self.radius = 9
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 180
        self.speed = 6.5
        angle = random.uniform(-math.pi/4, math.pi/4) - math.pi/2 # 위쪽 방향 무작위 각도
        self.vx = self.speed * math.cos(angle)
        self.vy = self.speed * math.sin(angle)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # 벽 충돌 (좌우)
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1
        elif self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.vx *= -1

        # 벽 충돌 (상단)
        if self.y - self.radius <= 60: # UI 영역 제외
            self.y = 60 + self.radius
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, WHITE, (int(self.x)-3, int(self.y)-3), 3) # 입체감 광택 효과

# ===== 벽돌 클래스 =====
class Brick:
    def __init__(self, x, y, width, height, color, points):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.points = points

# 벽돌 생성 함수
def init_bricks():
    bricks = []
    # 네온 컬러 오락실 감성 라인업
    colors = [(255, 50, 50), (255, 150, 0), (255, 230, 0), (50, 255, 50), (0, 150, 255)]
    rows, cols = 5, 8
    b_width, b_height = 74, 26
    pad_x, pad_y = 4, 4
    start_x = (WIDTH - (cols * (b_width + pad_x) - pad_x)) // 2
    start_y = 100

    for r in range(rows):
        for c in range(cols):
            x = start_x + c * (b_width + pad_x)
            y = start_y + r * (b_height + pad_y)
            points = (rows - r) * 10
            bricks.append(Brick(x, y, b_width, b_height, colors[r], points))
    return bricks

# 객체 생성
paddle = Paddle()
ball = Ball()
bricks = init_bricks()

# 폰트 세팅
font_main = pygame.font.SysFont("Segoe UI", 16, bold=True)
font_title = pygame.font.SysFont("Segoe UI", 36, bold=True)

# ===== 메인 게임 루프 =====
while True:
    screen.fill(BG_COLOR)
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if not game_over and not game_won:
        # 데이터 업데이트
        paddle.update()
        ball.update()
        update_particles()

        # 콤보 타이머 차감
        if combo_timer > 0:
            combo_timer -= 1
        else:
            combo = 0

        # 공이 바닥으로 낙하했을 때
        if ball.y + ball.radius >= HEIGHT:
            lives -= 1
            combo = 0
            if lives <= 0:
                game_over = True
            else:
                ball.reset()

        # 공 - 패들 충돌 검사
        ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius*2, ball.radius*2)
        if ball_rect.colliderect(paddle.rect) and ball.vy > 0:
            # 아케이드 각도 물리 엔진: 맞은 위치에 따라 꺾임 조절
            relative_intersect_x = paddle.rect.centerx - ball.x
            normalized_intersect_x = relative_intersect_x / (paddle.width / 2)
            bounce_angle = normalized_intersect_x * (math.pi / 3) # 최대 60도 회전
            
            ball.vx = -ball.speed * math.sin(bounce_angle)
            ball.vy = -ball.speed * math.cos(bounce_angle)

        # 공 - 벽돌 충돌 검사
        for brick in bricks[:]:
            if ball_rect.colliderect(brick.rect):
                # 파편 파티클 펑!
                create_particles(brick.rect.centerx, brick.rect.centery, brick.color)
                
                # 점수 계산 및 콤보 시스템
                combo += 1
                combo_timer = 45 # 콤보 유지 시간 (약 0.7초)
                score += brick.points * combo
                
                # 공 반사 방향 수학적 계산 (정교한 물리)
                # 좌우 면 충돌인지 상하 면 충돌인지 판별
                overlap_left = ball_rect.right - brick.rect.left
                overlap_right = brick.rect.right - ball_rect.left
                overlap_top = ball_rect.bottom - brick.rect.top
                overlap_bottom = brick.rect.bottom - ball_rect.top
                
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                
                if min_overlap == overlap_left or min_overlap == overlap_right:
                    ball.vx *= -1
                else:
                    ball.vy *= -1
                    
                bricks.remove(brick)
                break

        # 승리 조건
        if not bricks:
            game_won = True

    # ===== 오브젝트 그리기 =====
    # 1. 상단 점수 UI 바
    pygame.draw.rect(screen, (25, 25, 40), (0, 0, WIDTH, 60))
    pygame.draw.line(screen, (50, 50, 80), (0, 60), (WIDTH, 60), 2)
    
    score_lbl = font_main.render(f"SCORE: {score}", True, WHITE)
    lives_lbl = font_main.render(f"LIVES: {'♥' * lives}", True, (255, 50, 100))
    screen.blit(score_lbl, (20, 18))
    screen.blit(lives_lbl, (WIDTH - 130, 18))
    
    if combo > 1:
        combo_lbl = font_main.render(f"{combo} COMBO!", True, (255, 230, 0))
        screen.blit(combo_lbl, (WIDTH // 2 - combo_lbl.get_width() // 2, 18))

    # 2. 게임 메인 요소 그리기
    for brick in bricks:
        pygame.draw.rect(screen, brick.color, brick.rect, border_radius=4)
        pygame.draw.rect(screen, WHITE, brick.rect, width=1, border_radius=4) # 벽돌 테두리
        
    paddle.draw()
    ball.draw()
    draw_particles()

    # 3. 게임 오버 / 클리어 화면 텍스트
    if game_over or game_won:
        msg = "👑 YOU WIN! 👑" if game_won else "☠ GAME OVER ☠"
        color = (0, 255, 200) if game_won else (255, 0, 100)
        
        end_lbl = font_title.render(msg, True, color)
        screen.blit(end_lbl, (WIDTH // 2 - end_lbl.get_width() // 2, HEIGHT // 2 - 40))
        
        info_lbl = font_main.render(f"Final Score: {score}", True, WHITE)
        screen.blit(info_lbl, (WIDTH // 2 - info_lbl.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60) # 60 FPS 고정