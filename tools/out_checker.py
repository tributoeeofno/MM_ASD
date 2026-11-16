from pathlib import Path
import soundfile as sf

dataset_path = Path(
    "dataset/TOYADMOS2/generated/ToyCar_A1"
)

for wav_file in dataset_path.rglob("*.wav"):
    info = sf.info(wav_file)

    if (
        info.samplerate != 16000
        or info.channels != 1
        or info.frames != 192000
        or info.subtype != "PCM_16"
    ):
        print("CHECK:", wav_file, info)

print("Dataset inspection completed.")