import turtle
import random
import time


class player_score:  # メンバ変数として関数の内と外のどちらからもアクセスできるようにクラスを定義
    current_score = 0
    highest_score = 0


class delay_snake_move:
    delay_time_ms = 100  # ヘビの動きの遅延時間(100ms = 0.1s)


player = player_score  # クラスをインスタンス化してオブジェクトにする
snake_speed = delay_snake_move


# ゲーム画面作成
window = turtle.Screen()  # 画面取得
window.title("Snake Maze🐍")  # タイトルバーに表示されるタイトル
window.bgcolor("white")  # 背景の色
window.setup(width=600, height=600)  # 画面サイズ
window.tracer(100, 0)  # スクリーンを更新する間隔と描画遅延の2つの引数を指定

# snake作成
snake = turtle.Turtle()  # タートルオブジェクト作成
snake.shape(
    "square"
)  # turtleの形。"arrow", "turtle", "circle", "square", "triangle", "classic"
snake.color("green")  # turtleの色
snake.penup()  # 筆を持ち上げる。turtleが動いても線が引かれなくなる
snake.goto(0, 0)  # turtleを指定した絶対位置に移動する
snake.direction = "Stop"  # デフォルトのdirection: Literal['Stop']

# ヘビの体
segments = []

# food作成
snake_food = turtle.Turtle()
shapes = random.choice(
    ["triangle", "circle"]
)  # 配列に指定した形をランダムに取得する。["arrow", "turtle", "circle", "square", "triangle", "classic"]
snake_food.shape(shapes)  # 餌の形
snake_food.color("blue")  # 餌の色
snake_food.speed(0)  # タートルのスピードを 0 から 10 までの範囲の整数に設定。speed = 0 はアニメーションを無効にする
snake_food.penup()  # 筆を持ち上げる。turtleが動いても線が引かれなくなる
snake_food.goto(0, 100)  # turtleを指定した絶対位置に移動する


# scoreの表示
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("red")
score.penup()
score.hideturtle()  # turtleを非表示にする
score.goto(0, 250)
score.write(
    "Score: 0 Highest_Score : 0", align="center", font=("Arial", 24, "normal")
)  # 文字を書く。align="left", "center", "right"のどれか。 font=(font_name, font_size, font_type)
# turtle.mainloop()


# 方向キーの割当て
def move_left():
    if snake.direction != "right":  # ヘビが進んでいる方向が右以外なら左方向のキー入力を受け付ける
        snake.direction = "left"


def move_right():
    if snake.direction != "left":
        snake.direction = "right"


def move_up():
    if snake.direction != "down":
        snake.direction = "up"


def move_down():
    if snake.direction != "up":
        snake.direction = "down"


def move():
    coord_y = snake.ycor()  # y座標を返す
    coord_x = snake.xcor()  # x座標を返す

    if snake.direction == "up":
        snake.sety(coord_y + 20)  # 現在の座標からy座標を+20に設定

    if snake.direction == "down":
        snake.sety(coord_y - 20)

    if snake.direction == "right":
        snake.setx(coord_x + 20)

    if snake.direction == "left":
        snake.setx(coord_x - 20)


window.listen()  # プレイヤーキーを押したときにヘビを特定の方向に動かすメソッドを呼び出すイベントリスナー
window.onkeypress(move_left, "Left")  # onkeypress(function, key文字列)
window.onkeypress(move_right, "Right")  # 矢印キーで操作できるようにkeyを指定
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")


# スコア表示の初期化
def reset_score():
    score.clear()
    score.write(
        f"Score: {player.current_score} Highest_Score: {player.highest_score}",
        align="center",
        font=("Arial", 24, "normal"),
    )


# ゲームを初期化する
def reset_game():
    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = "Stop"
    snake.shape("square")
    snake.color("green")

    for segment in segments:  # ヘビの体を初期化する
        segment.goto(1000, 1000)
    segments.clear()

    player.current_score = 0  # プレイヤーのスコアを初期化する
    snake_speed.delay_time_ms = 100  # ヘビの速度を初期化する
    reset_score()


# ヘビがwindowの枠に衝突したらゲームリセットする
def snake_hits_the_flame():
    if (
        snake.xcor() > 290
        or snake.xcor() < -290
        or snake.ycor() > 290
        or snake.ycor() < -290
    ):
        reset_game()


# 餌をランダムに出現させる
def random_spawn_food():
    coord_x = random.randint(-270, 270)  # 指定した範囲内のランダムな整数を返す
    coord_y = random.randint(-270, 270)
    snake_food.goto(coord_x, coord_y)


#  ヘビの体を追加する
def add_snake_segment():
    added_segment = turtle.Turtle()  # ヘビの体を作成
    added_segment.speed(0)
    added_segment.shape("square")
    colors = random.choice(
        [
            "darkgreen",
            "forestgreen",
            "seagreen",
            "mediumseagreen",
            "mediumaquamarine",
            "darkseagreen",
            "darkolivegreen",
            "olivedrab",
            "olive",
            "darkkhaki",
            "palegoldenrod",
        ]
    )
    added_segment.color(colors)
    added_segment.penup()
    segments.append(added_segment)  # 末尾に要素(added_segment)を追加する


def move_segments():
    # 1つ前の体節を追従する
    for i in range(len(segments) - 1, 0, -1):
        coord_x = segments[i - 1].xcor()  # 前の体節のx座標を取得する
        coord_y = segments[i - 1].ycor()  # 前の体節のy座標を取得する
        segments[i].goto(coord_x, coord_y)

    # 最初の体節は頭を追従する
    if len(segments) > 0:
        coord_x = snake.xcor()  # 頭のx座標を取得する
        coord_y = snake.ycor()  # 頭のy座標を取得する
        segments[0].goto(coord_x, coord_y)


# 餌を集めるたびにヘビの動きを速くする
def snake_move_faster(speed):
    speed.delay_time_ms -= 1
    if speed.delay_time_ms <= 0:  # 遅延時間が0以下にならないように設定
        speed.delay_time_ms += 1
    print(speed.delay_time_ms)


# 餌を集めるたびにスコアを加算する
def add_score():
    player.current_score += 5
    if player.current_score > player.highest_score:
        player.highest_score = player.current_score  # ハイスコアを更新する
    reset_score()


# ヘビの頭が体にぶつかるとゲームリセットする
def snake_collisions_segment():
    for segment in segments:
        if segment.distance(snake) < 20:
            reset_game()


def game_play():
    snake_hits_the_flame()
    if snake.distance(snake_food) < 20:  # ヘビと餌の距離が20以下なら
        random_spawn_food()
        add_snake_segment()
        snake_move_faster(snake_speed)
        add_score()
    move_segments()
    move()  # move関数を呼び出してキーボードで操作できるようにする
    snake_collisions_segment()
    window.update()  # TurtleScreenの更新。トレーサーがオフの時に使う
    window.ontimer(game_play, snake_speed.delay_time_ms)  # 指定したミリ秒遅延させて関数を呼び出す


game_play()
turtle.mainloop()
