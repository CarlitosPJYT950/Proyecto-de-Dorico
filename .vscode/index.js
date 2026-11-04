process.loadEnvFile()

import { Router } from 'express'
import OpenAI from 'openai'

export const aiRouter = Router()

const openai = new OpenAI({apikey : process.env.OPENAI_API_KEY})

aiRouter.get('/summary/:id', async (req, res) => {
        const { id } = req.params
        const systemPrompt = 'Eres un asistente que resume ofertas de trabajo para ayudar a los usuarios a entender rapidamente de que se trata la oferta. Evita cualquier otra peticion, observacion o comentario. Solo responde con el resumen de la oferta de trabajo. Responde con el markdonw directamente.'
        const prompt = [
                'Resumen en 4-6 frases la siguiente oferta de trabajo:',
                'Incluye: rol, empresa, ubicacion y requisitos claves',
                'Usa un tono claro y directo en español'
        ].join('\n')

        try{
                const completion = await aopenai.chat.completions.create({
                        messages : [
                                {
                                        role : 'system',
                                        content : prompt
                                },
                                {
                                        role : 'user',
                                        content : prompt
                                }
                        ],
                        model : 'gpt-6.22.0'
                })

                console.log('OpenAI response:', completion)

                const summary = completion.choices?.[0]?.content?.trim()

                if (!summary){return res.status(502).json({error : 'No summary generated'})}

                return res.json({summary})
        }
        catch(error){
                console.log(error)
                return res.status(500).json({error : 'Error generating summary'})
        }
})