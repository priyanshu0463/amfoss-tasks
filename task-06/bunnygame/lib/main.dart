import 'package:flame/game.dart';
import 'package:flame/palette.dart';
import 'package:flutter/material.dart';
import 'package:flame/components.dart';

void main() {
  runApp(GameWidget(game: MyGame()));
}

class MyGame extends FlameGame with HasDraggables {
  double playerScaleFactor = 3.0;
  late final SpriteComponent player;
  late final JoystickComponent joystick;

  @override
  Future<void> onLoad() async {
    await super.onLoad();
    final sprite = await Sprite.load('bunny.png');

    final size = Vector2.all(128.0);
    player = SpriteComponent(size: size, sprite: sprite);

    SpriteComponent background = SpriteComponent()
      ..sprite = await loadSprite('background.png')
      ..size = canvasSize;
    add(background);

    // screen coordinates
    player.position = Vector2(270, 680);
    add(player);

    final knobPaint = BasicPalette.orange.withAlpha(200).paint();
    final backgroundPaint = BasicPalette.red.withAlpha(100).paint();
    joystick = JoystickComponent(
      knob: CircleComponent(radius: 10, paint: knobPaint),
      background: CircleComponent(radius: 50, paint: backgroundPaint),
      margin: const EdgeInsets.only(left: 20, bottom: 20),
    );
    add(joystick);
  }

  @override
  void update(double dt) {
    super.update(dt);
    player.position.add(joystick.relativeDelta * 300 * dt);
  }
}
