def combat(health, damage)
  if health <= 0
    return 0
  elsif damage <= 0
    return 0
  elsif (health - damage) < 0
    return 0
  else
    return health - damage
    end
end