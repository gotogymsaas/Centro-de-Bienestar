import { useTranslation } from 'next-i18next';

export default function Chat() {
  const { t } = useTranslation('common');
  return (
    <main className="min-h-screen flex items-center justify-center">
      <h1 className="text-2xl">{t('chat')}</h1>
    </main>
  );
}
