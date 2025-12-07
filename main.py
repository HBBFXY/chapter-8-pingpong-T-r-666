# 在这个文件里编写代码
import random

def judge_ball_winner(prob_a):
    random_value = random.random()
    return 'A' if random_value < prob_a else 'B'
def simulate_pingpong_game(prob_a):
    score_a, score_b = 0, 0
    serve_total = 0
    while True:
        current_server = 'A' if (serve_total // 2) % 2 == 0 else 'B'
        print(f"当前发球方：{current_server}", end=" | ")
        winner = judge_ball_winner(prob_a)
        if winner == 'A':
            score_a += 1
            print(f"得分方：A | 实时比分：A-{score_a} B-{score_b}")
        else:
            score_b += 1
            print(f"得分方：B | 实时比分：A-{score_a} B-{score_b}")
        serve_total += 1
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            break
        if (score_a == 12 and score_b == 10) or (score_b == 12 and score_a == 10):
            break
    return score_a, score_b
def main():
    random.seed(1024)
    print("===== 乒乓球比赛模拟程序 =====")
    while True:
        try:
            prob_a_input = float(input("请输入选手A每球得分的概率（0-1之间）："))
            if 0 <= prob_a_input <= 1:
                prob_a = prob_a_input
                prob_b = 1 - prob_a_input
                print(f"选手B每球得分概率自动计算为：{prob_b:.2f}")
                break
            else:
                print("输入错误！请输入0到1之间的数值")
        except ValueError:
            print("输入错误！请输入合法的数字")
    final_a, final_b = simulate_pingpong_game(prob_a)
    print("\n===== 本局比赛最终结果 =====")
    print(f"选手A最终得分：{final_a}")
    print(f"选手B最终得分：{final_b}")
    print(f"本局胜者：{'选手A' if final_a > final_b else '选手B'}")
if __name__ == "__main__":
    main()
