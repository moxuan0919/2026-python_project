"""main.py ─ 程式進入點（把 Game 和 ui 接起來）

【負責】C（介面與測試）
這個主迴圈已經寫好，只依賴 game.py / ui.py 的介面，C 可以直接用。
"""
from game import Game, Phase
import ui


def run() -> None:
    game = Game()
    while True:
        if game.phase == Phase.PLAYING:
            ui.show_status(game)
            ui.show_hand(game)
            action = ui.ask_action()
            indices = ui.ask_indices(len(game.hand))
            try:
                if action == "play":
                    ui.show_play_result(game.play(indices))
                else:
                    game.swap(indices)
            except ValueError as e:
                print(f"操作無效：{e}")

        elif game.phase == Phase.CHOOSE_UPGRADE:
            key = ui.ask_upgrade(game.upgrade_options)
            game.choose_upgrade(key)

        else:  # WON 或 LOST
            ui.show_summary(game.summary())
            if ui.ask_restart():
                game.restart()
            else:
                break


if __name__ == "__main__":
    run()
