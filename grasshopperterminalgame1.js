function Hero (name, position, health, damage, experience) {
    if (name == undefined){
      this.name = 'Hero'
    }
    else{
    this.name = name;
    }
    this.position = '00';
    this.health = 100;
    this.damage = 5;
    this.experience = 0;
}

