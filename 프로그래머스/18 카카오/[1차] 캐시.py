def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:  # cache hit
            cache.remove(city)
            cache.append(city)
            answer+=1
            
        else: # cache miss
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache.append(city)
                cache.pop(0)
            answer+=5
            
    return answer