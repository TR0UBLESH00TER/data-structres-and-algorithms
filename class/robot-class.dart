class robot {
  String name;
  String color;
  String model;

  Map info() {
    // Returns bot's information in the form of a Map.
    return {'name': this.name, 'color': this.color, 'model': this.model};
  }
}

main() {
  var r1 = robot();
  r1.name = 'Beep';
  r1.color = 'Blue';
  r1.model = 'alpha0.5';
  var r2 = robot();
  r2.name = 'Boop';
  r2.color = 'Grey';
  r2.model = 'alpha1.5';

  print("$r1 \n$r2\n");

  var r1info = r1.info();
  var r2info = r2.info();
  print("$r1info \n$r2info");
}
