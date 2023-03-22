import os
import numpy as np

#Generation for data augmentation

nb_gen = 2
pool = np.random.randint(10000, size=nb_gen)

subjects = ['man']
actions = ['runs', 'walks']
prompts = ['a *s *a forward', 'a *s *a around', 'a *s *a around and stops', 'a *s *a forward and stops']

for s in subjects:
    for a in actions:
        for p in prompts:
            pr = p.split('*s')
            pr2 = pr[1].split('*a')
            for i in range(0, nb_gen):
                print(pr[0] + s + pr2[0] + a + pr2[1])
                os.system("python -m sample.generate --model_path ./save/humanml_trans_enc_512/model000200000.pt --text_prompt \""+ pr[0] + s + pr2[0] + a + pr2[1] + "\" --seed " + str(pool[i]))