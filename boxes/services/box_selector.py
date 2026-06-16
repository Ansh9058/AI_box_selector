
from itertools import permutations
from boxes.models import Box
from products.models import Product

class BoxSelector:
    def recommend(self, items):
        total_weight=0
        total_volume=0
        products=[]

        for item in items:
            p=Product.objects.get(id=item['product_id'])
            qty=item['quantity']
            total_weight += p.weight*qty
            total_volume += p.length*p.width*p.height*qty
            products.extend([p]*qty)

        candidates=[]
        for box in Box.objects.filter(max_weight__gte=total_weight):
            box_volume=box.inner_length*box.inner_width*box.inner_height
            if box_volume < total_volume:
                continue

            valid=True
            for product in products:
                fits=False
                for l,w,h in set(permutations([product.length,product.width,product.height])):
                    if l<=box.inner_length and w<=box.inner_width and h<=box.inner_height:
                        fits=True
                        break
                if not fits:
                    valid=False
                    break

            if valid:
                waste=box_volume-total_volume
                candidates.append((float(box.cost),waste,box))

        if not candidates:
            return {"recommended_box":None,"message":"No suitable box found"}

        candidates.sort(key=lambda x:(x[0],x[1]))
        box=candidates[0][2]

        return {
            "recommended_box":{
                "id":box.id,
                "name":box.name,
                "cost":str(box.cost)
            }
        }
