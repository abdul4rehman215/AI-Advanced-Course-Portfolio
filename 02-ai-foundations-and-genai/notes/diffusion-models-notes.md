# Diffusion Models Notes

This part of the course introduced diffusion models through the example of Stable Diffusion and image generation.

The easiest way I understood diffusion is through the idea of adding and removing noise. In simple terms, diffusion models learn how to reconstruct useful visual structure from noisy inputs. This makes image generation feel much more understandable.

The course discussed two major stages:

## Forward Diffusion
In forward diffusion, noise is gradually added to an image until the original structure becomes hard to recognize.

## Reverse Diffusion
In reverse diffusion, the model learns how to reverse that noisy process and recover meaningful image structure step by step.

This reverse process is what enables generation from prompts.

Another important concept was latent diffusion. Instead of operating directly on every pixel at full size all the time, the model can work in a compressed internal representation. This makes the process more efficient and reduces computation cost.

The lecture also introduced **negative prompting**, which was one of the most practical ideas in this topic. A normal prompt tells the model what to generate. A negative prompt tells it what to avoid. This gives more control over artifacts, distortions, or unwanted visual properties.

This made it clear that image generation is not only about describing what you want, but also about guiding the system away from what you do not want.

The topic helped me understand:
- why diffusion models are different from traditional image pipelines
- why computation cost matters
- how prompt design affects image results
- why negative prompts improve control

Overall, this was a strong bridge between theory and the practical world of text-to-image AI systems.
